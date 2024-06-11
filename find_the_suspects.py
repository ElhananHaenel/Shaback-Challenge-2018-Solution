"""""
get the ip of suspects
"""""

id_of_suspects = [2449, 6796, 9237, 4024, 3538, 3608, 7239, 435, 5206, 2211]
ip = []

address = "log.csv"
input_file = open(addres, 'rb')
lines = []
for line in input_file:
    lines.append(line)



print len(lines)
for line in lines:
    #  print line
    y = line.split(",")

    if y[1] not in ip and int(y[0]) in x:
        ip.append(x[1])
input_file.close()

"""""
get the id that use the suspect ip
"""""

id_use_ip_of_suspect = []

address = "log.csv"
input_file = open(addres, 'r')
lines = input_file.read()
lines = lines.split('\n')
for line in lines:
    line = line.split(',')
    if len(line) > 2 and line[0] != "uid":
        if (line[1]) in ip and line[0] not in id_use_ip_of_suspect:
            id_use_ip_of_suspect.append(line[0])
input_file.close()

""""
print the num of ip the potential suspect used
"""""

num_of_ip_used = []

address = "log.csv"
input_file = open(addres, 'r')
lines = input_file.read()
lines = lines.split('\n')
for id in id_use_ip_of_suspect:
    for line in lines:
        line = line.split(',')
        if len(line) > 2 and line[0] != "uid":
            if (line[1]) in ip and line[1] not in num_of_ip_used and int(line[0]) == id:
                num_of_ip_used.append(line[1])
    print str(id), ":", str(len(num_of_ip_used))
input_file.close()

