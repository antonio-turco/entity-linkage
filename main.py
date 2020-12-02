from wrapper import Wrapper 
from wrapper_pipeline import RelationshipWrapper
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
relationship_wrapper = RelationshipWrapper(sites, wrapper)
print(relationship_wrapper.get_associations())