import os

obj_list = os.popen("ls *.nii | sed -e 's/\..*$//'")
str_list = obj_list.read()

str_list = str_list.split("\n")
str_list.remove('')
for i in range(0,len(str_list)):
    str_list[i] = int(str_list[i])
print(str_list)
str_list.sort()
i = 0
step = 4
while i < len(str_list):
    word = "ls " + str(str_list[i]) + ".nii.gz "+ str(str_list[i+1]) +".nii.gz " +str(str_list[i+2]) + ".nii.gz " +str(str_list[i+3]) + ".nii.gz"
    os.system(word+ " | parallel --jobs 4 recon-all -a {.} -i {} -all -qcache")
    print("4 data have been reconed!. next start\n")
    i+= step

print("well-done. enjoy:))")
