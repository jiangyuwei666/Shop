package com.test.service;

import com.test.BaseTest;
import com.test.dto.AppointExecution;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * Created By Jiangyuwei on 2019/8/18 12:41
 * Description:
 */
public class BookServiceImplTest extends BaseTest {

    @Autowired
    private BookService bookService;

    @Test
    public void testAppoint() throws Exception{
        long bookId = 1001;
        long studentId = 12345678910L;
        AppointExecution appointExecution = bookService.appoint(bookId, studentId);
        System.out.println(appointExecution);
    }

}
