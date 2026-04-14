#include <napi.h>           
#include <chrono>           
#include <string>   
#include "libxlsxwriter/include/xlsxwriter.h"
Napi::Number GenerateExcel(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();
    int rows = 10000;
    if (info.Length() > 0 && info[0].IsNumber()) {
        rows = info[0].As<Napi::Number>().Int32Value();
    }
    auto start = std::chrono::high_resolution_clock::now();
    std::string filename = "output_cpp.xlsx";

    lxw_workbook* workbook = workbook_new(filename.c_str());
    lxw_worksheet* sheet = workbook_add_worksheet(workbook, "Data");

    worksheet_write_string(sheet, 0, 0, "ID", NULL);//worksheet_write_string(лист, строка, колонка, текст, формат)
    worksheet_write_string(sheet, 0, 1, "Name", NULL);
    worksheet_write_string(sheet, 0, 2, "Value", NULL);
    for (int i = 1; i <= rows; ++i) {
        worksheet_write_number(sheet, i, 0, i, NULL);                        //ID
        std::string name = "Name_" + std::to_string(i);
        worksheet_write_string(sheet, i, 1, name.c_str(), NULL);             //Name
        worksheet_write_number(sheet, i, 2, i * 1.5, NULL);                  //Value; Value = ID * 1.5
    }
    workbook_close(workbook);
    auto end = std::chrono::high_resolution_clock::now();
    double elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    return Napi::Number::New(env, elapsed);
}
Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set(
        Napi::String::New(env, "generateExcel"),
        Napi::Function::New(env, GenerateExcel)
    );
    
    return exports;
}
NODE_API_MODULE(excel_addon, Init)