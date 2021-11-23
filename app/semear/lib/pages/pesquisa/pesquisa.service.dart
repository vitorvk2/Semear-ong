import 'dart:async';
import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:semear/envs.dart';
import 'package:semear/pages/home/home.dart';
import 'package:semear/paletas/paleta.dart';
import 'package:shared_preferences/shared_preferences.dart';

final TextEditingController searchController = TextEditingController();

Timer? timeToSearch;
List<dynamic> oficinasSearch = [];
List<int> oficinasSubscribed = [];

void onChangeSearch(String e, Function forceReload) {
  if (timeToSearch != null) {
    timeToSearch!.cancel();
  }

  timeToSearch = Timer(Duration(milliseconds: 450), () async {
    if (e == "") {
      return;
    }

    SharedPreferences prefs = await SharedPreferences.getInstance();

    http.Response request = await http.post(
      Uri.parse(url_semear + '/api/oficinas/getname/'),
      body: jsonEncode({
        'nome': e,
      }),
      headers: {
        'Authorization': 'Bearer ' + (prefs.getString('token') ?? ''),
        'validate': 'Bearer ' + (prefs.getString('validate') ?? '')
      },
    );

    Map<String, dynamic> dataJson = jsonDecode(request.body);

    oficinasSearch = dataJson['oficinas'];
    forceReload();
  });
}

Future subcribe(BuildContext context, Map<String, dynamic> oficina) async {
  showDialog(
    context: context,
    builder: (BuildContext ctx) {
      return AlertDialog(
        title: Text("Inscrever-se"),
        content: Text(
          "Deseja realmente se inscrever-se na oficina " +
              oficina['nome'] +
              "?",
        ),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.of(context).pop();
            },
            child: Padding(
              padding: const EdgeInsets.all(2.0),
              child: Text(
                "Cancelar",
                style: TextStyle(
                  fontSize: 14,
                  color: Colors.black,
                ),
              ),
            ),
            style: TextButton.styleFrom(
              backgroundColor: SemearColor[400],
            ),
          ),
          TextButton(
            onPressed: () async {
              sendSubToApi(context, oficina['id']);
            },
            child: Padding(
              padding: const EdgeInsets.all(2.0),
              child: Text(
                "Inscrever",
                style: TextStyle(
                  fontSize: 14,
                  color: Colors.white,
                ),
              ),
            ),
            style: TextButton.styleFrom(
              backgroundColor: Color(0xff020129),
            ),
          ),
        ],
      );
    },
  );
}

Future sendSubToApi(BuildContext context, int oficinaId) async {
  SharedPreferences prefs = await SharedPreferences.getInstance();

  await http.post(
    Uri.parse(url_semear + '/api/oficinasaluno/create/'),
    body: jsonEncode({
      'aluno_id': prefs.getInt('id_aluno') ?? 0,
      'oficina_id': oficinaId,
    }),
    headers: {
      'Authorization': 'Bearer ' + (prefs.getString('token') ?? ''),
      'validate': 'Bearer ' + (prefs.getString('validate') ?? '')
    },
  );

  Navigator.of(context).pushReplacement(CupertinoPageRoute(
    builder: (ctx2) => HomePage(),
  ));
}
