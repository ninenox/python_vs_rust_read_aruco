use opencv::{
    Result,
    prelude::*,
    highgui,
    imgproc,
    core::{self, Vector, Point2f},
    videoio,
    aruco::{self, DetectorParameters,Dictionary},
};

use std::time::{Instant};

fn find_aruco_markers(frame: &mut Mat,dict: core::Ptr::<Dictionary>){
    let mut gray = Mat::default();
        imgproc::cvt_color(frame, &mut gray, imgproc::COLOR_BGR2GRAY, 0).unwrap();
        
        let mut id  = Vector::<i32>::new();
        let mut cn  = Vector::<Vector::<Point2f>>::new();
        let mut rej  = core::no_array();
        let cm  = core::no_array();
        let dc  = core::no_array();
        let param = DetectorParameters::create().unwrap();

        aruco::detect_markers(
            &gray, 
            &dict, 
            &mut cn,
            &mut id,
            &param,
            &mut rej,
            &cm,
            &dc).unwrap();
        if id.len()>0 {
            aruco::draw_detected_markers(
                frame, 
                &cn, 
                &id, 
                core::Scalar::new(0f64, 255f64, 0f64, 0f64)).unwrap();
        }
        
}

fn main() -> Result<()> { // Note, this is anyhow::Result
    // Open a GUI window
    highgui::named_window("window", highgui::WINDOW_FULLSCREEN)?;
    // Open the web-camera (assuming you have one)
    let mut cam = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;
    
    let dictionary_ptr = aruco::get_predefined_dictionary(aruco::PREDEFINED_DICTIONARY_NAME::DICT_6X6_250)?;

    loop {
        let start = Instant::now();
        let mut frame = Mat::default();
        cam.read(&mut frame)?;
        find_aruco_markers(&mut frame, dictionary_ptr.clone());
        highgui::imshow("window", &frame)?;
        let key = highgui::wait_key(1)?;
        if key == 113 { // quit with q
            break;
        }
        let duration = start.elapsed();
        println!("Time elapsed : {:?}", duration);
    }
    Ok(())
}