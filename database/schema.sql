CREATE  TABLE  CLERKS (
   id          INT          NOT    NULL,
   login       VARCHAR(16)  NOT    NULL,
   first_name  VARCHAR(45)  NOT    NULL,
   last_name   VARCHAR(45)  NOT    NULL,
   password    VARCHAR(32)  NOT    NULL,
   PRIMARY     KEY          (id),
   UNIQUE      (login));
