# python_vs_rust_read_aruco

## Python (read Aruco)

Time elapsed : 0.03238415718078613 s<br>
Time elapsed : 0.03589653968811035 s<br>
Time elapsed : 0.03564810752868652 s<br>
Time elapsed : 0.02923154830932617 s<br>
Time elapsed : 0.03058075904846191 s<br>

## Rust (read Aruco)

Time elapsed : 33.734132 ms<br>
Time elapsed : 36.074481 ms<br>
Time elapsed : 29.200569 ms<br>
Time elapsed : 29.844299 ms<br>
Time elapsed : 32.337017 ms<br>

## การทดสอบ benchmark

เพื่อเปรียบเทียบความเร็วระหว่างโค้ด Python และ Rust สามารถใช้สคริปต์ **benchmark.sh** ที่อยู่ในรูทโปรเจกต์ได้ดังนี้

```bash
./benchmark.sh
```

สคริปต์จะรันโปรแกรมทั้งสองเวอร์ชันและรายงานเวลาที่ใช้ (หน่วยวินาที) สำหรับแต่ละภาษา

