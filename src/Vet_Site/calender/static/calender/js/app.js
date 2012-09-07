$(function () {
	var Event = Backbone.Model.extend()
	
	var Events = Backbone.Collection.extend({
		model: Event,
		url: '/api/v1/events/'
	});
	
	var EventsView = Backbone.View.extend({
		initialize: function(){
			_.bindAll(this);
			this.collection.bind('reset', this.addAll);
		},
		render: function(){
			$(this.el).fullCalendar({
				header: {
					left: 'prev,next today',
					center:'title',
					right: 'month,basicWeek,basicDay',
					ignoreTimezone: false
				},
				selectable: true,
				selectHelper: true,
				eventClick: this.eventClick
			});
			return this;
		},
		addAll: function(){
			$(this.el).fullCalendar('addEventSource', this.collection.toJSON());
		},
		eventClick: function(fcEvent) {
			var eventView = new EventView();
			eventView.model = this.collection.get(fcEvent.resource_uri)
			eventView.render();
		}
	});
	
	var EventView = Backbone.View.extend({
		el: $('#eventDialog'),
		initialize: function(){
			_.bindAll(this);
		},
		render: function() {
			$(this.el).dialog({
				modal: true,
				title: 'Event',
				buttons: {'Close': this.close},
				open: this.open
			})
			
			return this;
		},
		open: function(){
			this.$('#title').val(this.model.get('title'));
			this.$('#description').val(this.model.get('description'));
			if (!this.model.isNew()){
				var startTimezonePos = this.model.get('start').lastIndexOf('+')
				var startDateTimeSplit = this.model.get('start').indexOf('T');
				var endTimezonePos = this.model.get('end').lastIndexOf('+')
				var endDateTimeSplit = this.model.get('end').indexOf('T');
			
				this.$('#start-time').val(this.model.get('start').slice(startDateTimeSplit+1, startTimezonePos));
				this.$('#end-time').val(this.model.get('end').slice(endDateTimeSplit+1, endTimezonePos));
				this.$('#start-date').val(dateUnformat(this.model.get('start').slice(0, startDateTimeSplit)));
				this.$('#end-date').val(dateUnformat(this.model.get('end').slice(0, endDateTimeSplit)));
				
			}
		},
		close: function(){
			$(this.el).dialog("close");
		}
	});
	
	var events = new Events();
	new EventsView({el: $("#calendar"), collection: events}).render();
	events.fetch();
	
})
