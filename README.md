# DSCI551-Final-Project
我选择了5个东部的州，筛选完一共有30624个数据。我已经成功全部导入EC2 的mySQL！

这下面是我全部的码，jupyter notebook里面是所有的数据准备步骤，导出的csv都是由这个里面的码所导出的。如果你是一口气先导入，可以使用那个叫final dataset的，那个是没有分成表格的版本 

我的mysql结构如下，你也可以看sql file里面我的结构。py file里面是我的从csv导入mysql的码，不知道你是否用得上。但我都附到这里了。

Database 1: rental
- general_info (id, title, cityname, state, latitude, longitude)
- property_details (id, square_feet, bedrooms, bathrooms, pets_allowed)
- amenities (amenity_id, amenity_name) 
- property_amenities (id, amenity_id) 

Database 2: price
- pricing (id, price, currency)
- price_details (id, price_display, price_type)

Database 3: aptadditional
- media (id, has_photo)
- sources (id, source, time)
