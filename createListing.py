from dotenv import load_dotenv
import os
import requests
import csv

load_dotenv()

prefix = "https://www.michaels.com/api/mkp/v1/"
API_KEY = os.getenv("API_KEY")

filename = "listings.csv"
fields = []
parents = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Fields at the top of the CSV
    fields = next(csvreader)
    # Parent item right below the fields but above the children
    parents = next(csvreader)

    for row in csvreader:
        rows.append(row)
        print(row[0])

#Master_SKU,Quantity_Available (READ ONLY),Quantity,Bin_Location,Currency,Regular_Price,Discount_Price,Retail_Price,MAP_Price,Seller_Cost,Parent_SKU,Variation_Theme,Variation:Color,Variation:Size,Variation:Ribbon Width Simple,Variation:Saddle Stitch,Variation:pack quantity,Variation:Shabby Prints,Variation:RipLaces Cores,Variation:General Colors with Swatches,Variation:Printed Cotton Fabrics,Variation:Fabric Width,UPC,EAN,ISBN,ASIN,Locked,Title,Tags,Keywords,Brand,Manufacturer,Manufacturer_Part_Number,Lead_Time_To_Ship,Origin_Country,HS_Code,Status,Sort_Order,Thumbnail_Image,Main_Image,Main_Image_Alt_Text,Date_Created,Date_Updated,Description,Short_Description,link,Condition,Weight,Weight_Unit,Length,Width,Height,Dimensions_Unit,Package_Weight,Package_Weight_Unit,Package_Length,Package_Width,Package_Height,Package_Dimensions_Unit,Image_Extra_1,Image_Extra_1_Alt_Text,Image_Extra_2,Image_Extra_2_Alt_Text,Image_Extra_3,Image_Extra_3_Alt_Text,Image_Extra_4,Image_Extra_4_Alt_Text,Image_Extra_5,Image_Extra_5_Alt_Text,Image_Extra_6,Image_Extra_6_Alt_Text,Image_Extra_7,Image_Extra_7_Alt_Text,Image_Extra_8,Image_Extra_8_Alt_Text,Image_Extra_9,Image_Extra_9_Alt_Text,Image_Extra_10,Image_Extra_10_Alt_Text,Image_Extra_11,Image_Extra_11_Alt_Text,Image_Extra_12,Image_Extra_12_Alt_Text,Image_Extra_13,Image_Extra_13_Alt_Text,Image_Extra_14,Image_Extra_14_Alt_Text,Image_Extra_15,Image_Extra_15_Alt_Text,Image_Extra_16,Image_Extra_16_Alt_Text,Image_Extra_17,Image_Extra_17_Alt_Text,Image_Extra_18,Image_Extra_18_Alt_Text,Image_Extra_19,Image_Extra_19_Alt_Text,Image_Extra_20,Image_Extra_20_Alt_Text,Custom:product_bullet_point_4,Custom:product_bullet_point_5,Custom:product_bullet_point_1,Custom:product_bullet_point_2,Custom:product_bullet_point_3,Custom:amz-wmt-title,Custom:occasion,Custom:pattern_name,Custom:wmt-price,Custom:color_map,Custom:size,Custom:department_name,Custom:Color,"Custom:Color
#",Custom:color_name,Custom:item_package_quantity,Custom:material_type,Custom:size_name,Custom:unit_count,Custom:unit_count_type,Custom:catalog_number,Custom:special_features1,Custom:variation_theme,Custom:amz-price,Custom:material_type1,Custom:is_expiration_dated_product,Custom:Product_Type,Custom:Shopify_Tags,Custom:size_map,Custom:patern_name,Product_Components,amz-hbc:Template,amz-hbc:Restricted,amz-hbc:Disable Pricing,amz-hbc:Disable Inventory,amz-hbc:Price,amz-hbc:FBA_Price,amz-hbc:Floor_Price,amz-hbc:Ceiling_Price,amz-hbc:Category_1,amz-hbc:Category_2,amz-hbc:Item_Condition,amz-hbc:MAP_Preference,amz-hbc:Title,amz-hbc:Description,amz-hbc:Item_Type,amz-hbc:Bullet_1,amz-hbc:Bullet_2,amz-hbc:Bullet_3,amz-hbc:Bullet_4,amz-hbc:Bullet_5,amz-hbc:Search_Term_1,amz-hbc:Search_Term_2,amz-hbc:Search_Term_3,amz-hbc:Search_Term_4,amz-hbc:Search_Term_5,amz-hbc:Condition_Note,amz-hbc:Shipping_Group,amz-hbc:Business_Price,amz-hbc:Quantity_Price_Type,amz-hbc:Quantity_At_Or_Above_1,amz-hbc:Discounted_Price_1,amz-hbc:Quantity_At_Or_Above_2,amz-hbc:Discounted_Price_2,amz-hbc:Quantity_At_Or_Above_3,amz-hbc:Discounted_Price_3,amz-hbc:Quantity_At_Or_Above_4,amz-hbc:Discounted_Price_4,amz-hbc:Quantity_At_Or_Above_5,amz-hbc:Discounted_Price_5,amz-lello:Template,amz-lello:Restricted,amz-lello:Disable Pricing,amz-lello:Disable Inventory,amz-lello:Price,amz-lello:FBA_Price,amz-lello:Floor_Price,amz-lello:Ceiling_Price,amz-lello:Category_1,amz-lello:Category_2,amz-lello:Item_Condition,amz-lello:MAP_Preference,amz-lello:Title,amz-lello:Description,amz-lello:Item_Type,amz-lello:Bullet_1,amz-lello:Bullet_2,amz-lello:Bullet_3,amz-lello:Bullet_4,amz-lello:Bullet_5,amz-lello:Search_Term_1,amz-lello:Search_Term_2,amz-lello:Search_Term_3,amz-lello:Search_Term_4,amz-lello:Search_Term_5,amz-lello:Condition_Note,amz-lello:Shipping_Group,amz-lello:Business_Price,amz-lello:Quantity_Price_Type,amz-lello:Quantity_At_Or_Above_1,amz-lello:Discounted_Price_1,amz-lello:Quantity_At_Or_Above_2,amz-lello:Discounted_Price_2,amz-lello:Quantity_At_Or_Above_3,amz-lello:Discounted_Price_3,amz-lello:Quantity_At_Or_Above_4,amz-lello:Discounted_Price_4,amz-lello:Quantity_At_Or_Above_5,amz-lello:Discounted_Price_5,amz-lello:Attribute_Name_1,amz-lello:Attribute_Value_1,wmt:Template,wmt:Restricted,wmt:Disable Pricing,wmt:Disable Inventory,wmt:Price,wmt:Tax_Code,wmt:Floor_Price,wmt:Ceiling_Price,wmt:Category_1,wmt:Category_2,wmt:Title,wmt:Description,wmt:Key_Feature_1,wmt:Key_Feature_2,wmt:Key_Feature_3,wmt:Key_Feature_4,wmt:Key_Feature_5,wmt:Search_Term_1,wmt:Search_Term_2,wmt:Search_Term_3,wmt:Search_Term_4,wmt:Search_Term_5,wmt:Shipping_Group,wmt:Lead_Time,wmt:Attribute_Name_1,wmt:Attribute_Value_1,wmt:Attribute_Name_2,wmt:Attribute_Value_2,wmt:Attribute_Name_3,wmt:Attribute_Value_3

# response = requests.get(prefix + "listing",
#     headers={"Api-Key": API_KEY},
#     params={"taxonomyPath": "root//Shop Categories//Fabric & Sewing Shop//Fabrics//Apparel Fabric//Costume & Cosplay//Satin"}
#     )

# print(response.text)