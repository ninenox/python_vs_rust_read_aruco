# python_vs_rust_read_aruco

## Python (read Aruco)

Time elapsed : 32.38415718078613 ms<br>
Time elapsed : 35.89653968811035 ms<br>
Time elapsed : 35.64810752868652 ms<br>
Time elapsed : 29.23154830932617 ms<br>
Time elapsed : 30.58075904846191 ms<br>

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

