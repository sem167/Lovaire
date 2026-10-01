import json, sys
files = sys.argv[1:]
print(json.dumps({"themeId": "gid://shopify/OnlineStoreTheme/208207184211",
                  "files": [{"filename": f, "body": {"type": "TEXT", "value": json.dumps(json.load(open(f.replace("/", "__"))), ensure_ascii=False, separators=(",", ":"))}} for f in files]}, ensure_ascii=False))
