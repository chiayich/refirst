
function ObjGoodsTypeDiv(parentEle) {

    this.parentEle = parentEle;
    this.initElements();
    this.initEvent();
}

ObjSlideDiv.prototype = {

    constructor: ObjGoodsTypeDiv,

    initElements: function () {
        this.ulEle = $('<ul class="slide_pics"/>');
        this.ulElePoints = $('<ul class="points"/>');
        for (let i = 0; i < this.imglist.length; i++) {
            this.elementLi(this.imglist[i]);
        }
        this.prevEle = $('<div class="prev"/>');
        this.nextEle = $('<div class="next"/>');
        this.parentEle.append(this.ulEle);
        this.parentEle.append(this.ulElePoints);
        this.parentEle.append(this.prevEle);
        this.parentEle.append(this.nextEle);
        this.liEleList = this.ulEle.children();
        this.liPointList = this.ulElePoints.children();
        this.liactive();
    },

    elementLi: function (val) {
        this.liEle = $('<li/>');
        this.aEle = $('<a href=""/>');
        this.imgEle = $('<img src="/static/images/' + val + '"/>');
        this.aEle.append(this.imgEle);
        this.liEle.append(this.aEle);
        this.ulEle.append(this.liEle);

        this.liElePoint = $('<li/>');
        this.ulElePoints.append(this.liElePoint);
    },

    initEvent: function () {
        let that = this;
    },
    initParam: () => {
        let that = this;
        that.ulEle = $('<ul class="subnav f1/>"');
        $.ajax({
            url: 'goods/ajax_type_list',
            success: (data) => {
                that.elementLi(data.title);
            },
        });
    }

};