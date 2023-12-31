package servlet;

import java.io.IOException;
import java.io.PrintWriter;

import entity.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import service.UserService;
import service.impl.UserServiceImpl;

@WebServlet("/UserServlet")
public class UserServlet extends HttpServlet {
	private static final long serialVersionUID = 7308078748761515673L;

	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		String contextPath = request.getContextPath();
		String opr = request.getParameter("opr");
		UserService userService = new UserServiceImpl();
		try {
			if ("login".equals(opr)) {
				String uname = request.getParameter("uname");
				String password = request.getParameter("upwd");

				User user = new User();
				user.setUname(uname);
				user.setUpwd(password);
				user = userService.doLogin(user);
				if (user == null) {
					out.print("<script type=\"text/javascript\">");
					out.print("alert(\"用户名密码错误，请重新登录\");");
					out.print("open(\"" + contextPath + "/index.jsp\",\"_self\");");
					out.print("</script>");
				} else {
					request.getSession().setAttribute("admin", uname);
					response.sendRedirect(contextPath + "/util/news?opr=list");
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		out.flush();
		out.close();
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		this.doGet(request, response);
	}

}
