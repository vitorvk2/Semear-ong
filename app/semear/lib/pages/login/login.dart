import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:semear/pages/home/home.dart';
import 'package:semear/paletas/paleta.dart';

import 'login.service.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    checkLogin(context);
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(40.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "Semear",
                  style: TextStyle(fontSize: 40),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                Text("Login aluno", style: TextStyle(fontSize: 20)),
                Divider(
                  color: Color(0x01000001),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                TextField(
                  controller: user_ctrl,
                  decoration: InputDecoration(
                    hintText: "Usuário",
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(8)),
                    ),
                  ),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                TextField(
                  controller: password_ctrl,
                  obscureText: true,
                  decoration: InputDecoration(
                    hintText: "Senha",
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(8)),
                    ),
                  ),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                TextButton(
                  onPressed: () async {
                    print(await makeLogin(context));
                    if (await makeLogin(context)) {
                      Navigator.of(context).pushAndRemoveUntil(
                        CupertinoPageRoute(builder: (ctx) => HomePage()),
                        (router) => false,
                      );
                    }
                  },
                  child: Padding(
                    padding: const EdgeInsets.all(7.0),
                    child: Text(
                      "Entrar",
                      style: TextStyle(fontSize: 18, color: SemearColorDark),
                    ),
                  ),
                  style: TextButton.styleFrom(
                    backgroundColor: SemearColor[400],
                  ),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
