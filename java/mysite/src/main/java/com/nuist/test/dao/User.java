package com.nuist.test.dao;
// User.java

public class User {
	private int id;
	private String username;
	private String password; // 存储MD5加密后的密码
//	private Date createDate;
	private String createDate;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public User(int id, String username, String password, String date) {
		super();
		this.id = id;
		this.username = username;
		this.password = password;
		this.createDate = date;
	}

	public User() {
		super();
		// TODO Auto-generated constructor stub
	}

	@Override
	public String toString() {
		return "User [id=" + id + ", username=" + username + ", password=" + password + "]";
	}

	public String getCreateDate() {
		return createDate;
	}

	public void setCreateDate(String createDate) {
		this.createDate = createDate;
	}

}
