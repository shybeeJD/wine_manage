# wine_manage
@[TOC](WINE)

# Wine !


## 表
### 用户表
```
// An highlighted block
Users:{
	"id":1, //int, N
	"username":"shybee",//string, N
	"password":"123456",//string, N
	"phone":"17711112222"//string, N
	"register_time":"2021-07-12 16:41:20",//Datetime, default=now
}
```
### 地址表
```
// An highlighted block
Address:{
	"id":1,//int, N
	"name":"shybee",//string, N
	"phone":"17711112222",//string, N
	"label":"学校",//string, N
	"address":"湖北省武汉市武汉大学",//string, N
	"detial":"桂园四舍219",//string,N
	"delete":0,//int, default=0, 是否删除
	
}
```


### 商品表
```
// An highlighted block
Goods:{
	"id":2, //int, N, 商品id
	"title":"哈尔滨啤酒",//string, N
	"price":50, //int, N, 价格
	"stock":20, //int, N, 库存
	"category":"啤酒",//string, N, 种类
	"alcohol":"2.5",//string, N, 酒精度
	"capacity":"500",//string, N, 容量（ML）
	"brand":"哈尔滨",//string, N, 品牌
	"shelf_life":"360",//string, N, 天
	"pic":"pic1.jpg,pic2.jpg",//string, N, 图片路径(逗号分隔)
	"belong":5,//string, N, 所属仓库的id
	"delete":0,//int, default=0, 是否删除
	"add_time":"2021-07-12 16:41:20",//Datetime, default=now
}
```
### 配送表
```
// An highlighted block
DeliveryMan:{
	"id":1, //int, N
	"name":"shybee",//string, N
	"phone":"17711112222"//string, N
	"register_time":"2021-07-12 16:41:20",//Datetime, default=now
}
```
### 仓库表
```
// An highlighted block

//暂时不重要
Warehouse:{
	"id":5,//int, N, 仓库id
	"name":"武汉分仓库", //string, N, 仓库名字
	"city":"武汉", //string, N, 所在城市
	"lat":42,//int, N, 纬度
	"lng":117,//int, N, 经度
	"add_time":"2021-07-12 16:41:20",//Datetime, default=now
}
```

### 订单表
```
// An highlighted block

Order:{
	"id":"20210712162531", //string, N, 订单编号
	"user_id":5, //int, N, 用户id
	"status":1,//int, N, 订单状态
	"goods":"1:11,2:1,3:1,4:1",//string, N, 购买的商品(id:数量，逗号隔开) 
	"goods_price":100,//int, N, 商品费用
	"packings_price":10,//int, N, 打包费用
	"delivery_price":5,//int, N, 外送费用
	"discount":20,//int, N, 红包优惠
	"address":int //int, N, 配送地址id
	"delivery_man":id,//int, Y, 配送员
	"payment_channels":1,//int, N, 支付渠道
	"add_time":"2021-07-12 16:41:20",//Datetime, default=now
	
	""
}

"status":{
	1: 订单已完成
	2: 正在配送
	3: 商家已接单
	4: 商家拒绝接单
	5: 等待支付
	6: 取消支付
	7: 正在退款
}
"payment_channels:{
	1:在线支付
	2:线下支付
}
```

