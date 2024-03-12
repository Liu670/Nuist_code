package test;

import java.io.InputStream;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.apache.log4j.Logger;
import org.junit.Test;

public class UserMapperTest {

	private Logger logger = Logger.getLogger(UserMapperTest.class);

	@Test
	public void testSelectCount() {
		// 1. 读取全局配置文件 mybatis-config.xml
		String resource = "mybatis-config.xml";
		SqlSession sqlSession = null;
		try {
			// 2. 获取配置文件的输入流
			InputStream is = Resources.getResourceAsStream(resource);
			// 3. 创建 sqlsessionFactory 对象 进行配置文件的读取
			SqlSessionFactory factory = new SqlSessionFactoryBuilder().build(is);
			// 4. 创建 sqlsession 对象 调用 mapper 文件进行数据操作
			sqlSession = factory.openSession();
			int count = 0; // 查询结果
			// mybatis通过 mapper 文件的 namespace和子元素的 id 查询对应的 sql
			count = sqlSession.selectOne("mapper.userMapper.selectCount");
			logger.debug(count);

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			sqlSession.close();
		}

	}

}
