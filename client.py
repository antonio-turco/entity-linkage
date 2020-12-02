from wrapper import Wrapper 
import itertools

def log(message):
	print("[DEBUG]: " + message)

wrapper = Wrapper()

siteA = [
	(0, "john-wall-rotoworld.html"),
	(1, "danilo-gallinari-rotoworld.html"),
	(2, "luguentz-dort-rotoworld.html"),
]

siteB = [
	(3, "danilo-gallinari-nba.html"),
	(4, "john-wall-nba.html"),
	(5, "luguentz-dort-nba.html"),
]

sites = [siteA, siteB]
leaves_sites = []

#estraggo termini foglia per ogni link
for site in sites:
	site_leaves = []
	for page in site:
		log("extracting from: " + page[1])
		extracted_leaves = wrapper.get_all_leaves(page[1])
		#ad ogni termine ci associo la pagina sorgente
		labeled_leaves = wrapper.assoc_key_to_leaves(page[0], extracted_leaves)
		site_leaves.append(labeled_leaves)
		log("leaves extracted")
	leaves_sites.append(site_leaves)


#estraggo le differenze negli stessi siti
unique_leaves_sites = []
for leaves_site in leaves_sites:
	unique_leaves_site = wrapper.diff(leaves_site)
	unique_leaves_sites.append(unique_leaves_site)

#associo le pagine inter-sito in base alla similiarità

'''

siteA
siteB

for page1 in siteA
	for page2 in siteB
		similiarity(site1, site2)
		

similiarity(site1, site2):
	len(intersection([site1, site2]))/(len(site1) + len(site2))

'''
def similiarity(page1, page2):
	intersection = wrapper.intersection([page1, page2])
	return len(intersection)/(len(page1) + len(page2))

siteA = unique_leaves_sites[0]
siteB = unique_leaves_sites[1]

for page1 in siteA:
	max_sim = 0
	max_key1 = 0
	max_key2 = 0
	for page2 in siteB:
		key1 = page1[0][0]
		key2 = page2[0][0]
		sim = similiarity(page1, page2)
		if sim > max_sim:
			max_sim = sim
			max_key1 = key1
			max_key2 = key2
	log("page " + str(max_key1) + " is associated with " + str(max_key2))

