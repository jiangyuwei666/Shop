package com.test.entity;

/**
 * Created By Jiangyuwei on 2019/8/17 10:17
 * Description:
 */
public class Book {

    private long bookId;
    private String name;
    private int number;
    public long test;

    public Book() {
    }

    public Book(long bookId, String name, int number) {
        System.out.println("************" + bookId + "***********");
        this.test = bookId;
        this.bookId = bookId;
        this.name = name;
        this.number = number;
        System.out.println("************" + this.bookId + "***********");
    }

    public long getBookId() {
        return bookId;
    }

    public void setBookId(long bookId) {
        this.bookId = bookId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    @Override
    public String toString() {
        return "Book{" +
                "bookId=" + bookId +
                ", name='" + name + '\'' +
                ", number=" + number +
                '}';
    }
}
