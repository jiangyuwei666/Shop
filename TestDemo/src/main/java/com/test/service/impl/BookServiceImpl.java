package com.test.service.impl;

import com.test.dao.AppointmentDao;
import com.test.dao.BookDao;
import com.test.dto.AppointExecution;
import com.test.entity.Appointment;
import com.test.entity.Book;
import com.test.enums.AppointStateEnum;
import com.test.exception.AppointException;
import com.test.exception.NoNumberException;
import com.test.exception.RepeatAppointException;
import com.test.service.BookService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * Created By Jiangyuwei on 2019/8/18 10:50
 * Description:
 */
@Service
public class BookServiceImpl implements BookService {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private BookDao bookDao;
    @Autowired
    private AppointmentDao appointmentDao;

    @Override
    public Book getById(long bookId) {
        return bookDao.queryById(bookId);
    }

    @Override
    public List<Book> getList() {
        return bookDao.queryAll(0, 1000);
    }

    @Override
    @Transactional // 事务注解
    public AppointExecution appoint(long bookId, long studentId) {

        try{
            int update = bookDao.reduceNumber(bookId);// 减少书库存
            if (update <= 0)
                throw new NoNumberException("no number");
            else {
                int insert = appointmentDao.insertAppointment(bookId, studentId);
                if (insert <= 0)
                    throw new RepeatAppointException("repeat appoint");
                else {
                    Appointment appointment = appointmentDao.queryByKeyWithBook(bookId, studentId);
                    return new AppointExecution(bookId, AppointStateEnum.SUCCESS, appointment);
                }
            }
        }
        catch (NoNumberException e){
            throw e;
        }catch (RepeatAppointException e){
            throw e;
        }catch (Exception e){
            logger.error(e.getMessage(), e);
            throw new AppointException(e.getMessage());
        }
    }
}
