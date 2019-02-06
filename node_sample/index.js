var XLSX = require( 'xlsx' );


// ファイル読み込み
var book = XLSX.readFile( './SalesSample.xlsx' );

// シート
var sheet1 = book.Sheets["Sheet1"];
console.log( sheet1 );

// sheet1["C13"] = { v: 1.01, t: 'n', w: '1.01' };

// book.Sheets["Sheet1"] = sheet1;
// XLSX.writeFile( book, './SalesSample.xlsx', { type: 'xlsx' } );