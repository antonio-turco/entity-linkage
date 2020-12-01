import requests
from lxml import html

class Wrapper:

	def get_all_leaves(self, url):
		page = requests.get(url)
		dom_tree = html.fromstring(page.text)
		all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
		return all_leaves

	def assoc_key_to_leaves(self, key, leaves):
		return list(map(lambda leave: (key, leave), leaves))