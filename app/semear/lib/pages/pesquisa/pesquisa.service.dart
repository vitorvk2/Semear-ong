import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:semear/envs.dart';
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
