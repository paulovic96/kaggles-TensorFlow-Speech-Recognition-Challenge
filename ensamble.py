import csv
import numpy as np

with open("predictions/prediction_v5.4csv", "r") as p1:
	with open("predictions/prediction_v50.csv", "r") as p2:
		with open("predictions/prediction_v51.csv", "r") as p3:
			with open("predictions/prediction_v48.csv", "r") as p4:
				with open("predictions/ensamble.csv", "w") as ensamble:
					p1_reader = csv.reader(p1, delimiter=",", dialect="unix", quoting = csv.QUOTE_NONE)
					p2_reader = csv.reader(p2, delimiter=",", dialect="unix", quoting = csv.QUOTE_NONE)
					p3_reader = csv.reader(p3, delimiter=",", dialect="unix", quoting = csv.QUOTE_NONE)
					p4_reader = csv.reader(p4, delimiter=",", dialect="unix", quoting = csv.QUOTE_NONE)

					csv_writer = csv.writer(ensamble, delimiter=",", dialect="unix", quoting = csv.QUOTE_NONE)

					for a,b,c,d in zip(p1_reader,p2_reader, p3_reader,p4_reader ):
						unique,pos = np.unique([a[1],b[1],c[1], d[1]],return_inverse=True)
						counts = np.bincount(pos) 
						maxpos = counts.argmax()  

						csv_writer.writerow([a[0], unique[maxpos]]) 	