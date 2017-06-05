/**
 * Created by chiayich on 6/3/17.
 */

ObjLabelA = (goods_type_id, sort_way) => {
    this.gt_id = goods_type_id;
    this.sort_way = sort_way;
    this.initElements();
    this.initEvent();
};

ObjLabelA.prototype = {
    constructor: ObjLabelA,

    initElements: () => {
        let data = this.fetch();

    },

    initEvent: () => {

    },

    fetch: () => {
        this.param = {
            'goods_type': this.gt_id,
            'sort_way': this.sort_way,
        };
       $.ajax({
           url: '/df_goods/goods_new/',
           type: 'GET',
           data: this.param,
           dataType: 'json',
           success: (data)=> {
               console.log('[SUCCESS] : ')
           },
           error: (data)=> {
               console.log('[ERROR] : ');
               console.log(data);
           }
       }) ;
    },
};