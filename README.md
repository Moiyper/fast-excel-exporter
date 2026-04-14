#Fast Excel Exporter – C++ Node.js Addon

Generate a 10,000-row Excel file **50x faster** than pure JavaScript.

##Benchmark

| Method                  | Time (10,000 rows) |
|-------------------------|--------------------|
| **JavaScript (xlsx)**   | ~3500 ms           |
| **This C++ addon**      | **~60 ms**         |

> 📸 *Screenshot: console output showing C++ generation in 60 ms.*

##How it works

This is a native Node.js addon written in C++ using:
- [libxlsxwriter](https://github.com/jmcnamara/libxlsxwriter) – high-performance Excel generation
- Node-API (`node-addon-api`) – stable ABI for Node.js

Heavy operations (memory allocation, ZIP compression, XML generation) are executed in C++, bypassing the JavaScript event loop entirely.

##Installation & Build

```cmd:

git clone https://github.com/Moiyper/fast-excel-exporter.git
cd fast-excel-exporter
npm install
node-gyp configure
node-gyp build```
