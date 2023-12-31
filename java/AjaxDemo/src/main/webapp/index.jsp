<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
    <!--
 * @Author: xiaoliu
 * @Date: 2023-12-04 13:59:26
 * @LastEditors: xiaoliu
 * @LastEditTime: 2023-12-04 15:51:48
 * @Description: file content
 * @FilePath: /code/Web/AJAX/index1.html
-->
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="icon" href="http://liu.ihong.love:81/favicon.ico">
        <style>
            * {
                padding: 0;
                margin: 0;
            }
        </style>
    </head>
    <script src="http://liu.ihong.love:81/file/html/js/jquery-3.7.1.js  "></script>

    <body>
        <form action="UserServlet" id="myForm">
            <table>
                <tr>
                    <td>用户名：</td>
                    <td><input type="text" name="name" id="name" onblur="validate()">
                        <font color="red">*</font>
                    </td>
                    <td>
                        <div id="nameDiv" style="display: inline-block;"></div>
                    </td>
                </tr>
                <tr>
                    <td>邮箱：</td>
                    <td><input type="email" name="name" id="name">
                        <font color="red">*</font>
                    </td>
                    <td></td>
                </tr>
                <tr></tr>
                <tr>
                    <td colspan="3">
                        <input type="submit" name="" id="">
                    </td>
                </tr>
            </table>
        </form>
    </body>

    </html>
    <script>
        function validate() {
            var name = $("#name").val();
            if (name == null || name == "") {
                $("#nameDiv").html("用户名不能为空");
            } else {
                // 创建XMLHttpRequest对象
                var XMLHttpRequest = createXmlHttpRequest();
                // 设置回调函数
                XMLHttpRequest.onreadystatechange = callback;
                // 初始化请求
                var url = "UserServlet?name=" + name;
                XMLHttpRequest.open("POST", url, true);
                // 发送请求
                XMLHttpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                XMLHttpRequest.send("test=111&test2=222");
                //XMLHttpRequest.send(null);
                function callback() {
                    if (XMLHttpRequest.readyState == 4 && XMLHttpRequest.status == 200) {
                        var result = XMLHttpRequest.responseText;
                        if (result == "true") {
                            $("#nameDiv").html("用户名已被使用");
                        } else {
                            $("#nameDiv").html("用户名可用");
                        }
                    }
                }
            }
        }
        function createXmlHttpRequest() {
            // ie7以上及其他浏览器
            if (window.XMLHttpRequest) {
                // 创建XMLHttpRequest对象
                return new XMLHttpRequest();
            } else {
                // ie5  ie6
                return new ActiveXObject("Microsoft.XMLHTTP");
            }
        }

    </script>