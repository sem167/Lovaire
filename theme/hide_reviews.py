"""Reviews (nog) niet tonen: reviewsectie op home en productpagina en de sterren onder de producttitel weg.
Sterren in kaarten en koopblok staan uit via de instelling show_rating (standaard uit). Draai als laatste."""
import json
load = lambda f: json.load(open(f))
def save(f, d): json.dump(d, open(f, "w"), ensure_ascii=False, indent=2)

idx = load("templates__index.json")
idx["sections"].pop("reviews", None)
idx["order"] = [k for k in idx["order"] if k != "reviews"]
save("templates__index.json", idx)

prod = load("templates__product.json")
prod["sections"].pop("reviews", None)
prod["order"] = [k for k in prod["order"] if k != "reviews"]
det = prod["sections"]["main"]["blocks"]["product-details"]
det["blocks"].pop("rating", None)
det["block_order"] = [k for k in det["block_order"] if k != "rating"]
save("templates__product.json", prod)
print("home", idx["order"]); print("product", prod["order"], det["block_order"])
