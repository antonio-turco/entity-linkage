import requests
from lxml import html

class Wrapper:

	def get_all_leaves(self, url):
		page = requests.get(url)
		dom_tree = html.fromstring(page.text)
		all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
		return all_leaves

	def assoc_key_to_leaves(self, key, leaves):
		return list(map(lambda leaf: (key, leaf), leaves))

	def remove_key_from_leaves(self, leaves):
		return list(map(lambda key, leaf: leaf, leaves))

	def intersection(self, site_leaves):
		print(site_leaves[0])
		intersection = set(self.remove_key_from_leaves(site_leaves[0]))
		for site in site_leaves:
			leaves_set = set(self.remove_key_from_leaves(site))
			intersection = intersection & leaves_set

	def get_unique_leaves(self, site_leaves, intersection):
		return []

	def diff(self, site_leaves):
		intersection = self.intersection(site_leaves)
		return self.get_unique_leaves(site_leaves, intersection)