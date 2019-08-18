package com.test.exception;

/**
 * Created By Jiangyuwei on 2019/8/18 11:03
 * Description:
 */
public class NoNumberException extends RuntimeException {

    public NoNumberException(String message) {
        super(message);
    }

    public NoNumberException(String message, Throwable cause) {
        super(message, cause);
    }

}
