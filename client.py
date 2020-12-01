from wrapper import Wrapper 
import itertools

def log(message):
	print("[DEBUG]: " + message)

wrapper = Wrapper()

siteA = [
	(0, "https://www.imdb.com/title/tt6723592/?ref_=fn_al_tt_1"),
	(1,"https://www.imdb.com/title/tt0209144/?ref_=nv_sr_srsg_0"),
]

siteB = [
	(2, "https://www.rottentomatoes.com/m/memento"),
	(3, "https://www.rottentomatoes.com/m/tenet"),
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

'''
for leave in leaves:
	for text in leave:
		print(text[0])
'''

for leaves_site in leaves_sites:
	wrapper.diff(leaves_site)

#estraggo le differenze negli stessi siti

#associo le pagine inter-sito in base alla similiarità
