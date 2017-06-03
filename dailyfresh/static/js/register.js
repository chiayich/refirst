$(function () {

    var error_name = false;
    var error_password = false;
    var error_check_password = false;
    var error_email = false;
    var error_check = false;


    $('#user_name').blur(function () {
        check_user_name();
    });

    $('#pwd').blur(function () {
        check_pwd();
    });

    $('#c_pwd').blur(function () {
        check_cpwd();
    });

    $('#email').blur(function () {
        check_email();
    });

    $('#allow').click(function () {
        if ($(this).is(':checked')) {
            error_check = false;
            $(this).siblings('span').hide();
        }
        else {
            error_check = true;
            $(this).siblings('span').html('请勾选同意');
            $(this).siblings('span').show();
        }
    });


    function check_user_name() {
        var user_name_el = $('#user_name');
        var len = user_name_el.val().length;
        if (len < 5 || len > 20) {
            user_name_el.next().html('请输入5-20个字符的用户名');
            user_name_el.next().show();
            error_name = true;
        } else {
            user_name_el.next().hide();
            error_name = false;
        }
    }

    function check_pwd() {
        var password_el = $('#pwd');
        var len = password_el.val().length;
        if (len < 8 || len > 20) {
            password_el.next().html('密码最少8位，最长20位');
            password_el.next().show();
            error_password = true;
        } else {
            password_el.next().hide();
            error_password = false;
        }
    }


    function check_cpwd() {
        console.log('check_cpwd');
        var pass = $('#pwd').val();
        var cpass_el = $('#c_pwd');
        var cpass = cpass_el.val();

        if (pass != cpass) {
            cpass_el.next().html('两次输入的密码不一致');
            cpass_el.next().show();
            error_check_password = true;
        }
        else {
            cpass_el.next().hide();
            error_check_password = false;
        }

    }

    function check_email() {
        console.log('check_email');
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        var email_el = $('#email');
        if (re.test(email_el.val())) {
            email_el.next().hide();
            error_email = false;
        }
        else {
            email_el.next().html('你输入的邮箱格式不正确');
            email_el.next().show();
            error_check_password = true;
        }

    }


    $('#reg_form').submit(function () {
        check_user_name();
        check_pwd();
        check_cpwd();
        check_email();
        return judge_form_value()
    });

    function judge_form_value() {
        console.log('judge_form_value');
        return error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false
    }
});