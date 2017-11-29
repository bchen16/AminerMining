import sys

with open('AMiner-Author.txt','r') as f:
	lines = list(f.readlines())
d = {}
key = ['univ','inc','corp','scho','lab','service','research','inst','Education']
for i in lines:
	if len(i) > 10:
		if i[1] == 'a':
			raw = i[3:-1]
			raw = raw.split(';')
			for j in raw:
				temp = j.split(', ')
				for k in range(0,len(temp)):
					t = ''
					for l in key:
						if l in temp[k].lower():
							t = t + ',' + temp[k]
						else:
							d[t] = temp[k+1:]
univ_place={}
univ_country={}

country_replace=["USA","U.S.A",'United States',"Canada","Albania","Andorra","Armenia","Austria","Azerbaijan","Belarus"
           ,"Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Cyprus","Czech Republic","Denmark",
           "Estonia","Finland","France","Georgia","Germany","Greece","Hungary","Iceland","Ireland","Italy",
           "Kazakhstan","Kosovo","Latvia","Liechtenstein","Lithuania","Luxembourg","Macedonia","Malta","Moldova"
           ,"Monaco","Montenegro","Netherlands","Norway","Poland","Portugal","Romania","Russia","San Marino","Serbia"
           ,"Slovakia","Slovenia","Spain","Sweden","Switzerland","Turkey","Ukraine","United Kingdom","UK","U.K.",
           "united kingdom","Vatican City","Afghanistan","Armenia","Azerbaijan","Bahrain","Bangladesh","Bhutan","Brunei","Cambodia",
           "China","Cyprus","Georgia","India","Indonesia","Iran","Iraq","Israel","Japan","Jordan","Kazakhstan",
           "Kuwait","Kyrgyzstan","Laos","Lebanon","Malaysia","Maldives","Mongolia","Myanmar","Nepal","North Korea",
           "Korea","Oman","Pakistan","Palestine","Philippines","Qatar","Russia","Saudi Arabia","Singapore","South Korea",
           "Sri Lanka","Syria","Taiwan","Tajikistan","Thailand","Timor-Leste","Turkey","Turkmenistan",
           "United Arab Emirates","UAE","Uzbekistan","Vietnam","Yemen","Antigua and Barbuda","Bahamas","Barbados",
           "Belize","Costa Rica","Cuba","Dominica","Dominican Republic","El Salvador","Grenada","Guatemala",
           "Haiti","Honduras","Jamaica","Mexico","Nicaragua","Panama","Saint Kitts and Nevis","Saint Lucia",
           "Saint Vincent and the Grenadines","Trinidad and Tobago","United States of America","Argentina",
           "Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay",
           "Venezuela","Australia","Fiji","Kiribati","Marshall Islands","Micronesia","Nauru","New Zealand",
           "Palau","Papua New Guinea","Samoa","Solomon Islands","Tonga","Tuvalu","Vanuatu","Algeria","Angola",
           "Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic","CAR",
           "Chad","Comoros","Democratic Republic of the Congo","Republic of the Congo","Cote d'Ivoire",
           "Djibouti","Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon","Gambia","Ghana","Guinea",
           "Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania",
           "Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Rwanda","Sao Tome and Principe",
           "Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan","Sudan","Swaziland",
           "Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]

US_state_replace=["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
                  "Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
                  "Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi",
                  "Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
                  "New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
                  "Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
US_abb_replace=["AK","AL","AR","AZ","CA","CO","CT","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA",
                      "MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK",
                      "OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]

for univ, country in d.items():
    if country !=[""] and country !=[]:
        univ_country[univ]=country[-1:][0]
        for i in country_replace:
            if i in str(country):
                univ_country[univ]=i
        for i in US_state_replace:
            if i in univ_country[univ]:
                univ_country[univ]='USA'
        for i in US_abb_replace:
            if i == univ_country[univ]:
                univ_country[univ]='USA'
        
univ_country

