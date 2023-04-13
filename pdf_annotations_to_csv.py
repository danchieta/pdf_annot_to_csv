from PyPDF2 import PdfReader

# Set the input and output files here
input_filename = "tlosf_paper_20230118 - annotated.pdf"
output_filename = "outfile.csv"

# you shouldn't need to change anything below this line
reader = PdfReader(input_filename )
out = open(output_filename,'w')

out.write('Content;Type;PageNum\n')
pagenum = 1
stypes = list()
for page in reader.pages:
    if "/Annots" in page :
        for annot in page["/Annots"] :
            obj = annot.get_object()
            stypes.append(obj["/Subtype"])
            if obj["/Subtype"] == "/FreeText" or \
                obj["/Subtype"] == "/Text" or \
                obj["/Subtype"] == "/FreeText" or \
                obj["/Subtype"] == "/Caret":
                content = obj["/Contents"].replace('\n',' ').replace('  ',' ')

                s = "{};{};{}\n".format(content,obj["/Subtype"][1:],pagenum)
                print(s)
                # annotation = {"page":pagenum, "subtype": obj["/Subtype"],"contents": obj["/Contents"]}
                # print(annotation)
                out.write(s)
                a = obj
    else:
        print('No annotations in page {}'.format(pagenum))
    pagenum = pagenum + 1
out.close()
