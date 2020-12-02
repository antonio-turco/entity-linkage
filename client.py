from wrapper import Wrapper 
import itertools

def log(message):
	print("[DEBUG]: " + message)

wrapper = Wrapper()

siteA = [
	(0, "dataset/john-wall-rotoworld.html"),
	(1, "dataset/luguentz-dort-rotoworld.html"),
	(2, "dataset/danilo-gallinari-rotoworld.html"),
]

siteB = [
	(3, "dataset/danilo-gallinari-nba.html"),
	(4, "dataset/john-wall-nba.html"),
	(5, "dataset/luguentz-dort-nba.html"),
]

sites = [siteA, siteB]
leaves_sites = []

#estraggo termini foglia per ogni link
for site in sites:
	site_leaves = []
	for label, page in site:
		log("extracting from: " + page)
		extracted_leaves = wrapper.get_all_leaves(page)
		site_leaves.append( (label, extracted_leaves) )
		log("leaves extracted")
	leaves_sites.append(site_leaves)


#estraggo le differenze negli stessi siti
unique_leaves_sites = []
for leaves_site in leaves_sites:
	unique_leaves_site = wrapper.diff(leaves_site)
	unique_leaves_sites.append(unique_leaves_site)

#associo le pagine inter-sito in base alla similiarità
def similiarity(page1, page2):
	intersection = wrapper.intersection([page1, page2])
	return len(intersection)/(len(page1) + len(page2))

siteA = unique_leaves_sites[0]
siteB = unique_leaves_sites[1]

for label1, page1 in siteA:
	max_sim = 0
	max_label1 = 0
	max_label2 = 0
	for label2, page2 in siteB:
		sim = similiarity(page1, page2)
		if sim > max_sim:
			max_sim = sim
			max_label1 = label1
			max_label2 = label2
	log("page " + str(max_label1) + " is associated with " + str(max_label2))

