package com.test.exception;

/**
 * Created By Jiangyuwei on 2019/8/18 11:03
 * Description:
 */
public class RepeatAppointException extends RuntimeException {

    public RepeatAppointException(String message) {
        super(message);
    }

    public RepeatAppointException(String message, Throwable cause) {
        super(message, cause);
    }

}
