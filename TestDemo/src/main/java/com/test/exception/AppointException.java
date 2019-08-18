package com.test.exception;

/**
 * Created By Jiangyuwei on 2019/8/18 11:04
 * Description:
 */
public class AppointException extends RuntimeException {

    public AppointException(String message) {
        super(message);
    }

    public AppointException(String message, Throwable cause) {
        super(message, cause);
    }

}
