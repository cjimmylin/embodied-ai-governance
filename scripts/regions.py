"""Country code -> region mappings used throughout. Codes follow ISO 3166-1 alpha-2 plus EU, INT, XX."""
import country_converter as coco, pandas as pd
_cc=coco.CountryConverter()
SPECIAL={"EU":("European Union","Europe","Europe","supranational"),"INT":("International","International","International","international"),
         "XX":("Unknown","Unknown","Unknown","unknown"),"UK":("United Kingdom","Europe","Northern Europe","national"),"EL":("Greece","Europe","Southern Europe","national")}
# study regions mirror the collection folders but are assigned from jurisdiction, not folder
def study_region(continent,unregion,code):
    if code in ("EU",): return "Europe"
    if code=="INT": return "International"
    if code=="XX": return "Unknown"
    if continent=="Europe": return "Europe"
    if continent=="Africa": return "Africa"
    if continent=="Oceania": return "Oceania"
    if continent=="Asia":
        if unregion=="Western Asia" or code in ("IR","TR","IL","PS","EG"): return "Middle East"
        return "Asia"
    if continent=="America":
        if code in ("US","CA","GL"): return "North America"
        return "Latin America & Caribbean"
    return "Unknown"
def lookup(code):
    code=(code or "XX").strip().upper()
    if code in SPECIAL:
        n,cont,unr,_=SPECIAL[code]; return {"country_name":n,"continent":cont,"un_subregion":unr,"study_region":study_region(cont,unr,code)}
    name=_cc.convert(code,src="ISO2",to="name_short",not_found=None)
    if name is None: return {"country_name":code,"continent":"Unknown","un_subregion":"Unknown","study_region":"Unknown"}
    cont=_cc.convert(code,src="ISO2",to="continent",not_found="Unknown"); unr=_cc.convert(code,src="ISO2",to="UNregion",not_found="Unknown")
    # Egypt is African continent but Middle East in this study's collection design; keep Africa (continent) but flag study_region as Middle East? Keep continent-based: Africa.
    return {"country_name":name,"continent":cont,"un_subregion":unr,"study_region":study_region(cont,unr,code)}
if __name__=="__main__":
    for c in ["KR","US","BR","EG","IL","TR","RU","AU","EU","INT","XX","GB","CA","AE","ZA","MX","IN","JP","CN","GL"]: print(c,lookup(c))
