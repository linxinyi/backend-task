from geopy import Point, distance
import pandas as pd
import os


def ProductSearch(condition):
    print os.getcwd()
    product_list = pd.read_csv('../data/products.csv')
    shop_list = pd.read_csv('../data/shops.csv')
    tagging_list = pd.read_csv('../data/taggings.csv')
    tag_list = pd.read_csv('../data/tags.csv')

    count = condition['count']
    lat = condition['position']['lat']
    lng = condition['position']['lng']
    radius = condition['radius']
    tags = condition['tags']

    original = Point(float(lat), float(lng))

    # find the list of shops inside the radius
    shop = shop_list[shop_list.apply(lambda x: distance.distance(Point(x['lat'], x['lng']), original).meters <= radius, axis=1)]

    # find the corresponding tag_id for the given tag
    tag = tag_list[tag_list.apply(lambda x: x['tag'] in tags, axis=1)]

    # eliminate the shops which don't contain the given tags
    if not tag.empty:
        # find the taggings contains the given tag_id
        tagging = tagging_list[tagging_list.apply(lambda x: x['tag_id'] in list(tag['id']), axis=1)]

        # find the shops contains the tags
        shop_tag = shop[shop.apply(lambda x: x['id'] in list(tagging['shop_id']), axis=1)]

    # find the products inside this shops and eliminate the products which quantity equal to 0
    product = product_list[product_list.apply(lambda x: x['shop_id'] in list(shop_tag['id']) and x['quantity'] != 0, axis=1)]

    # sort the products according to popularity
    product_sorted = product.sort_values(['popularity'], ascending=0)

    print product_sorted.head(count)
    data = product_sorted.head(count).to_json(orient='records', lines=True)[1:-1].replace('},{', '} {')
    # return  most popular products
    return data

if __name__ == '__main__':

    condition = {'count': 3, 'position': {u'lat': 59.33258, u'lng': 18.0649}, 'radius': 100, 'tags': [u'casual']}
    ProductSearch(condition)
