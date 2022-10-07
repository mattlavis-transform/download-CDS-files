def parse_date(d):
    d2 = d[6:8] + "/" + d[4:6] + "/" + d[0:4]
    return d2


def xml_to_xlsx_filename(filename):
    return "CDS updates " + xml_to_file_date(filename) + ".xlsx"


# export-20221006T000000_20221006T235959-20221007T001536.xml
def xml_to_file_date(filename):
    filename = "export-20221006T000000_20221006T235959-20221007T001536.xml"
    xml_date_part = filename.split("T")[0].split("-")[1]

    year = xml_date_part[0:4]
    month = xml_date_part[4:6]
    day = xml_date_part[6:]

    return year + "-" + month + "-" + day
