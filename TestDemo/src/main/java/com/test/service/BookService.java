package com.test.service;

import com.test.dto.AppointExecution;
import com.test.entity.Book;

import java.util.List;

/**
 * Created By Jiangyuwei on 2019/8/18 10:49
 * Description:
 */
public interface BookService {

    /**
     * 查询一本图书
     *
     * @param bookId
     * @return
     */
    Book getById(long bookId);

    /**
     * 查询所有图书
     *
     * @return
     */
    List<Book> getList();

    /**
     * 预约图书
     *
     * @param bookId
     * @param studentId
     * @return
     */
    AppointExecution appoint(long bookId, long studentId);


}
