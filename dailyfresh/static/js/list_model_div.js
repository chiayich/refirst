/**
 * Created by chiayich on 6/3/17.
 */
//类别划分　参数　类别
function ListModelDiv(ls, pEle){
    this.tid = ls[0];  // 类别　id
    this.ttitle = ls[1]; // 类别名称
    this.img_show = ls[2]; // 图片路径
    this.pEle = pEle;  // 父级别元素　id
    this.initElements();
}

ListModelDiv.prototype = {

    constructor: ListModelDiv,

    initElements: function (){

        this.list_model = $('<div class="list_model"/>');
        this.listTitle();
        this.list_model.append(this.list_title);
        this.initGoodsCon();
        this.list_model.append(this.goods_con);
        this.pEle.append(this.list_model);
    },

    listTitle: function(){

        this.list_title = $('<div class="list_title clearfix"/>');
        this.list_title.append($('<h3 class="fl" id="model01">'+ this.ttitle+'</h3>'));
        this.list_new = $('<div class="subtitle fl"><span>|</span></div>');

        $.ajax({
            url: '/df_goods/new_show',
            type: 'GET',
            data: {'tid': this.tid},
            dataType: 'json',
            success: (data) => {
                let ele_msg = JSON.parse(data.message);
            $.each(ele_msg, (index, item)=>{
                this.list_new.append($('<a href="#">' +item.fields.title + '</a>'));
            });
            },
        });


        this.list_title.append(this.list_new);
        this.list_title.append($('<a href="/df_goods/more_list/?tid=' + this.tid + '" class="goods_more fr" id="fruit_more">查看更多 >></a>'));
    },

    initGoodsCon: function() {

        this.goods_con = $('<div class="goods_con clearfix"/>');
        this.goods_con.append($('<div class="goods_banner fl"><img src="/static/' + this.img_show + '"></div>'));
        this.goods_list = $('<ul class="goods_list fl"/>');
        $.ajax({
            url: '/df_goods/hot_show',
            type: 'GET',
            data: {'tid':this.tid},
            dataType: 'json',
            success: (data) => {
                let field_set = JSON.parse(data.data);
                $.each(field_set, (index, item) => {
                        let ele = '<li><h4><a href="#">'+ item.fields.title +'</a></h4>' +
                            '<a href="#"><img src="/static/' + item.fields.pic+ '"/></a>' +
                            '<div class="prize">'+ item.fields.price +'</div>' +
                            '</li>';
                        this.goods_list.append($(ele));
                    });
                this.goods_con.append(this.goods_list);
                },
        });

    },
};