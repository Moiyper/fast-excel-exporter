const addon = require('./build/Release/excel_addon');

console.log('🚀 Генерируем Excel на 10 000 строк через C++...');
const timeMs = addon.generateExcel(10000);
console.log(`✅ Готово! Время выполнения: ${timeMs} мс (${(timeMs / 1000).toFixed(2)} сек)`);