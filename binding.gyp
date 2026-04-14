{
  "targets": [
    {
      "target_name": "excel_addon",
      "sources": [
        "excel_addon.cpp",
        "libxlsxwriter/src/app.c",
        "libxlsxwriter/src/chart.c",
        "libxlsxwriter/src/chartsheet.c",
        "libxlsxwriter/src/comment.c",
        "libxlsxwriter/src/content_types.c",
        "libxlsxwriter/src/core.c",
        "libxlsxwriter/src/custom.c",
        "libxlsxwriter/src/drawing.c",
        "libxlsxwriter/src/format.c",
        "libxlsxwriter/src/hash_table.c",
        "libxlsxwriter/src/metadata.c",
        "libxlsxwriter/src/packager.c",
        "libxlsxwriter/src/relationships.c",
        "libxlsxwriter/src/rich_value.c",
        "libxlsxwriter/src/rich_value_rel.c",
        "libxlsxwriter/src/rich_value_structure.c",
        "libxlsxwriter/src/rich_value_types.c",
        "libxlsxwriter/src/shared_strings.c",
        "libxlsxwriter/src/styles.c",
        "libxlsxwriter/src/table.c",
        "libxlsxwriter/src/theme.c",
        "libxlsxwriter/src/utility.c",
        "libxlsxwriter/src/vml.c",
        "libxlsxwriter/src/workbook.c",
        "libxlsxwriter/src/worksheet.c",
        "libxlsxwriter/src/xmlwriter.c",
	"libxlsxwriter/third_party/minizip/ioapi.c",
	"libxlsxwriter/third_party/minizip/zip.c",
	"libxlsxwriter/third_party/minizip/iowin32.c"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "libxlsxwriter/include",
        "libxlsxwriter/src",
	"libxlsxwriter/third_party/minizip",
	"libxlsxwriter/third_party/minizip/zip"
      ],
      "defines": [
        "NAPI_DISABLE_CPP_EXCEPTIONS",
        "USE_STANDARD_TMPFILE"
      ],
      "conditions": [
        ["OS=='win'", {
          "defines": [
            "_CRT_SECURE_NO_WARNINGS"
          ]
        }]
      ]
    }
  ]
}