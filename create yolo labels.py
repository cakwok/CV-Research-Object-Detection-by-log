folder = "/Users/casca/Library/Mobile Documents/com~apple~CloudDocs/Northeastern Courses/CV Fish Research/FISH_resized/valid/"
f = open(folder + "validation.csv", "r")
for line in f:
    dst_path = folder + "labels/" + line.split(",")[0].split(".jpg")[0] + ".txt"
    print(dst_path)
    #converted = "0 " + str(float(line.split(",")[1])/600) + " " +  str(float(line.split(",")[2])/400) + " " +  str(float(line.split(",")[3])/600) + " " +  str(float(line.split(",")[4])/400)
    converted = "0 " + str(line.split(",")[1]) + " " + str(line.split(",")[2]) + " " + str(line.split(",")[3]) + " " + str(line.split(",")[4])
    f2 = open(dst_path, "w")
    f2.write(converted)
f.close()
