package com.test.entity;

import java.util.Date;

/**
 * Created By Jiangyuwei on 2019/8/17 10:19
 * Description:
 */
public class Appointment {

    private long bookId;
    private long studentID;
    private Date appointTime;

    private Book book;

    public Appointment() {
    }

    public Appointment(long bookId, long studentID, Date appointTime, Book book) {
        this.bookId = bookId;
        this.studentID = studentID;
        this.appointTime = appointTime;
        this.book = book;
    }

    public long getBookId() {
        return bookId;
    }

    public void setBookId(long bookId) {
        this.bookId = bookId;
    }

    public long getStudentID() {
        return studentID;
    }

    public void setStudentID(long studentID) {
        this.studentID = studentID;
    }

    public Date getAppointTime() {
        return appointTime;
    }

    public void setAppointTime(Date appointTime) {
        this.appointTime = appointTime;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }

    @Override
    public String toString() {
        return "Appointment{" +
                "bookId=" + bookId +
                ", studentID=" + studentID +
                ", appointTime=" + appointTime +
                ", book=" + book +
                '}';
    }
}
