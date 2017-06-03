
function ObjSlideDiv(imglist, parentEle) {

    this.imglist = imglist;
    this.nowli = 0;
    this.prevli = 0;
    this.parentEle = parentEle;
    this.initElements();
    this.initEvent();
}

ObjSlideDiv.prototype = {

    constructor: ObjSlideDiv,

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
        this.liEleList.not(':first').css({'left': 760});

        this.prevEle.on('click', function () {
            if (that.ismove) {
                return;
            }
            that.ismove = true;
            that.nowli--;
            that.imove();
            that.liactive();
        });

        this.nextEle.on('click', function () {
            if (that.ismove) {
                return;
            }
            that.ismove = true;
            that.nowli++;
            that.imove();
            that.liactive();
        });
        this.liPointList.on('click', function () {
            that.nowli = $(this).index();
            if (that.nowli == that.prevli) {
                return;
            }
            $(this).addClass('active').siblings().removeClass('active');
            that.imove();
        });
        this.timer = setInterval(function () {
            that.slideEvnt(that)
        }, 3000);
        this.parentEle.on('mouseenter', function () {
            clearInterval(that.timer);
        });
        this.parentEle.on('mouseleave', function () {
            that.timer = setInterval(function () {
                that.slideEvnt(that)
            }, 3000);
        });

    },

    liactive: function () {
        this.liPointList.eq(this.nowli).addClass('active').siblings().removeClass('active');
    },

    imove: function () {
        if (this.nowli < 0) {
            this.nowli = this.liEleList.length - 1;
            this.prevli = 0;
            this.moveright();
            return;
        }
        if (this.nowli > this.liEleList.length - 1) {
            this.nowli = 0;
            this.prevli = this.liEleList.length - 1;
            this.moveleft();
            return;
        }


        if (this.nowli > this.prevli) {
            this.moveleft();
        } else {
            this.moveright();
        }
    },

    moveleft: function () {
        this.liEleList.eq(this.nowli).css({"left": -760});
        this.liEleList.eq(this.nowli).animate({"left": 0});
        this.liEleList.eq(this.prevli).animate({'left': 760}, this.stopSlide(this));
        this.prevli = this.nowli;
    },

    moveright: function () {
        this.liEleList.eq(this.nowli).css({'left': 760});
        this.liEleList.eq(this.nowli).animate({'left': 0});
        this.liEleList.eq(this.prevli).animate({'left': -760}, this.stopSlide(this));
        this.prevli = this.nowli;
    },

    stopSlide: function (obj) {
        obj.ismove = false;
    },

    slideEvnt: function (obj) {
        if (obj.ismove) {
            return;
        }
        obj.ismove = true;
        obj.nowli++;
        obj.imove();
        obj.liactive();
    },

};