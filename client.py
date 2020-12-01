import requests
from lxml import html


#page = requests.get("https://www.amazon.it/deal/4d61aab4?showVariations=true&smid=A11IL2PNWYJU7H&pf_rd_r=WCTQ011G7N6HDA4SWJMD&pf_rd_p=ea5bf4a9-15d4-4a5e-bb3a-0866177c4312")
#tree = html.fromstring(page.text)

#all_leaves = tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")

#print(all_leaves)

def get_all_leaves(url):
	page = requests.get(url)
	dom_tree = html.fromstring(page.text)
	all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
	return all_leaves

print(
	get_all_leaves("https://www.amazon.it/deal/4d61aab4?showVariations=true&smid=A11IL2PNWYJU7H&pf_rd_r=WCTQ011G7N6HDA4SWJMD&pf_rd_p=ea5bf4a9-15d4-4a5e-bb3a-0866177c4312")
)