/*
 * @Author: xiaoliu
 * @Date: 2023-12-11 23:14:33
 * @LastEditors: xiaoliu
 * @LastEditTime: 2023-12-14 20:17:27
 * @Description: file content
 * @FilePath: /code/Java/MyWebSiteDemo/src/main/java/com/nuist/test/filter/MyFilter.java
 */
package com.nuist.test.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

//在过滤器类上方加上注解@WebFilter ,然后依然通过/* 表示拦截所有请求
//@WebFilter("/*")
public class MyFilter implements Filter {
	@Override
	public void init(FilterConfig filterConfig) throws ServletException {

	}

	@Override
	public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
			throws IOException, ServletException {
		// // 统一处理请求和响应的乱码
		servletRequest.setCharacterEncoding("utf-8");
		servletResponse.setCharacterEncoding("utf-8");
		// servletResponse.setContentType("text/html;charset=utf-8");
		// 处理过后放行
		filterChain.doFilter(servletRequest, servletResponse);

	}

	@Override
	public void destroy() {

	}
}