package com.test.web;

import com.test.dto.AppointExecution;
import com.test.dto.Result;
import com.test.entity.Book;
import com.test.enums.AppointStateEnum;
import com.test.exception.NoNumberException;
import com.test.exception.RepeatAppointException;
import com.test.service.BookService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

/**
 * Created By Jiangyuwei on 2019/8/18 12:50
 * Description:
 */
@RestController
@RequestMapping("/test")
public class BookController {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private BookService bookService;

    @RequestMapping("/list")
    private List list(){
        List<Book> list = bookService.getList();
        System.out.println("********************");
        System.out.println(list);
        return list;
    }

}
