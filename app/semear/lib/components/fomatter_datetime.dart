import 'package:flutter/material.dart';

class FormatterDateTimeComponent extends StatelessWidget {
  FormatterDateTimeComponent({
    required this.date,
    this.style = const TextStyle(),
  });

  final String date;
  final TextStyle style;

  String splitDatetime(String date) {
    List<String> datetimeSplit = date.split(".")[0].split("T");
    List<String> dateSplit = datetimeSplit[0].split("-");
    List<String> timeSplit = datetimeSplit[1].split(":");

    dateSplit.reversed;

    return dateSplit.join("/") + " " + timeSplit[0] + ":" + timeSplit[1];
  }

  @override
  Widget build(BuildContext context) {
    return Text(
      splitDatetime(date),
      style: style,
    );
  }
}
