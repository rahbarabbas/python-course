from dputils import scrape

# step 1: get the data as soup onject
# step 2: create the setup dictionaries
# step 3: pass the dictionaries into the extract_many() function
# step 4: repeat step 1 to step 3 until data keep moving
# step 5: check and save data into a file

# step 1:
query='laptop'
pos=1
url=f'https://www.flipkart.com/search?q={query}&page={pos}'
soup=scrape.get_webpage_data(url)

# step 2:
#target dict,item dict,etc
t={'tag':'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}}
rep_items={'tag':'div','attrs':{'class':'_1AtVbE col-12-12'}}
title={'tag':'div','attrs':{'class':'_4rR01T'}}
price={'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
link={'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'}

pos=1
all_data=[]
while True:
    

